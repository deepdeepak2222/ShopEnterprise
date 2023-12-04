from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_inventory', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
                  ALTER TABLE shop_inventory_shopitem ADD COLUMN tsv tsvector GENERATED ALWAYS AS (
                    setweight(to_tsvector('english', coalesce(name, '')), 'A') ||
                    setweight(to_tsvector('english', coalesce(barcode, '')), 'B') ||
                    setweight(to_tsvector('english', coalesce(description,'')), 'C')
                  ) STORED;
                  CREATE INDEX IF NOT EXISTS gin_shopitem_tsv ON shop_inventory_shopitem USING gin(tsv);
                ''',

            reverse_sql='''
                  ALTER TABLE shop_inventory_shopitem DROP COLUMN tsv;
                '''
        ),
    ]