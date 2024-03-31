import datetime

my_host = "localhost"


def create_public_tenant():
    from customers.models import Client
    url = f"{my_host}"  # "my-domain.com"
    # create your public tenant
    tenant = Client(domain_url=url,
                    # don't add your port or www here! on a local server you'll want to use localhost here
                    schema_name='public',
                    name='Schemas Inc.',
                    paid_until='2030-12-05',
                    on_trial=False)
    tenant.save()


def create_real_tenant(tenant_name, tenant_code, admin_email, admin_phone, password, paid_until='2030-12-05'):
    from customers.models import Client
    from rest_auth.models import AdminUser
    url = f"{tenant_code}.{my_host}"
    # create your first real tenant
    Client.objects.get_or_create(schema_name=tenant_code, name=tenant_name, defaults={
        "domain_url": url,  # don't add your port or www here!
        "paid_until": paid_until,
        "on_trial": True
    })  # # migrate_schemas automatically called, your tenant is ready to be used!
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("set schema %s", [tenant_code])
        now = str(datetime.datetime.now().date())
        cursor.execute("INSERT INTO rest_auth_adminuser"
                       "(username, email, phone, password, is_superuser, first_name, last_name, is_staff, is_active, "
                       "date_joined) "
                       "VALUES(%s, %s, %s, %s, %s, 'f_name', 'l_name', false, true, %s)",
                       [admin_email, admin_email, admin_phone, password, True, now])


# create_public_tenant()
create_real_tenant("dt1", "dt1", "deepdeepak2222+1@gmail.com", "8817648997", "password")
