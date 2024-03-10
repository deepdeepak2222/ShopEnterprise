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


def create_real_tenant(tenant_name, tenant_code, paid_until='2030-12-05'):
    from customers.models import Client
    url = f"{tenant_code}.{my_host}"
    # create your first real tenant
    tenant = Client(domain_url=url,  # don't add your port or www here!
                    schema_name=tenant_code,
                    name=tenant_name,
                    paid_until=paid_until,
                    on_trial=True)
    tenant.save()  # migrate_schemas automatically called, your tenant is ready to be used!
