from rest_framework import viewsets
from django.shortcuts import render
from .models import *
from .serializers import *


def show_api_data(request):
    return render(request, 'core/show_data.html')

def show_banner_crud(request):
    return render(request, 'core/show_banner_crud.html')

def show_image_menu_crud(request):
    return render(request, 'core/show_image_menu_crud.html')

def show_menu_detail_crud(request):
    return render(request, 'core/show_menu_detail_crud.html')

def CarouselImageAPI(request):
    return render(request, 'core/CarouselImageAPI.html')

def MenuClickToLoadMenuDetail(request):
    return render(request, 'core/MenuClickToLoadMenuDetail.html')



def ListProductWithAddToCartCheckoutOrder(request):
    return render(request, 'core/ListProductWithAddToCartCheckoutOrder.html')

class TblBannerView(viewsets.ModelViewSet):
    queryset = TblBanner.objects.all()
    serializer_class = TblBannerSerializer

class ImageTypeView(viewsets.ModelViewSet):
    queryset = ImageType.objects.all()
    serializer_class = ImageTypeSerializer

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetailView(viewsets.ModelViewSet):
    queryset = MenuDetail.objects.all()
    serializer_class = MenuDetailSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('categoryID')
        if category_id:
            queryset = queryset.filter(categoryID_id=category_id)
        return queryset
    
class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('productID')
        if product_id:
            return ProductDetail.objects.filter(productID=product_id)
        return ProductDetail.objects.all()
    
class ProductDetailImageViewSet(viewsets.ModelViewSet):
    queryset = ProductDetailImage.objects.all()
    serializer_class = ProductDetailImageSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('productID')
        if product_id:
            return self.queryset.filter(productID__id=product_id)
        return self.queryset



class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

