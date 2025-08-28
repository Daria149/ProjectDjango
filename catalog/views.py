from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, ModeratorForm
from catalog.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect



class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ModeratorForm
        raise PermissionDenied



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def post(self, request, *args, **kwargs):
        product_id = kwargs['pk']
        product = get_object_or_404(Product, id=product_id)
        if not request.user.has_perm('catalog.delete_product') or self.request.user != self.object.owner:
            raise PermissionDenied
        product.delete()


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        product_list = Product.objects.filter(publish_product=True)
        return product_list


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

