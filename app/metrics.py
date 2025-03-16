from products.models import Product
from categories.models import Category
from inflows.models import Inflow
from outflows.models import Outflow




def get_product_metrics():
    products = Product.objects.all()
    
    vehicles_total_quantity = sum(product.quantity for product in products if product.category and product.category.name == 'Veículos')
    equipment_total_quantity = sum(product.quantity for product in products if product.category and product.category.name == 'Equipamentos')
    security_devices_total_quantity = sum(product.quantity for product in products if product.category and product.category.name == 'Dispositivos de Segurança')
    
    recent_inflows = Inflow.objects.all().order_by('-created_at')[:10]
    recent_outflows = Outflow.objects.all().order_by('-created_at')[:10]

    
    inflows_data = [{'product': inflow.product.title, 'quantity': inflow.quantity} for inflow in recent_inflows]
    outflows_data = [{'product': outflow.product.title, 'quantity': outflow.quantity} for outflow in recent_outflows]

    return dict(
        vehicles_total_quantity=vehicles_total_quantity,
        equipment_total_quantity=equipment_total_quantity,
        security_devices_total_quantity=security_devices_total_quantity,
        recent_inflows=inflows_data,  
        recent_outflows=outflows_data,
    )
  


     