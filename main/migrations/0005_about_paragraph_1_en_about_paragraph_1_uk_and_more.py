# Generated by Django 4.1.2 on 2022-10-26 19:00

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_about_banner_contacts_info_partners_testimonials_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='paragraph_1_en',
            field=models.TextField(blank=True, db_index=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='paragraph_1_uk',
            field=models.TextField(blank=True, db_index=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='paragraph_2_en',
            field=models.TextField(blank=True, db_index=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='paragraph_2_uk',
            field=models.TextField(blank=True, db_index=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_line_1_en',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_line_1_uk',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_line_2_en',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_line_2_uk',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='about_short_en',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='about_short_uk',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='address_en',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='address_uk',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_en',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_uk',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='open_hours_en',
            field=ckeditor.fields.RichTextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='open_hours_uk',
            field=ckeditor.fields.RichTextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='subscribe_text_en',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='subscribe_text_uk',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='text_en',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='text_uk',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='about_title_line_1_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='about_title_line_1_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='about_title_line_2_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='about_title_line_2_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='contact_title_line_1_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='contact_title_line_1_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='contact_title_line_2_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='contact_title_line_2_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='main_title_line_1_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='main_title_line_1_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='main_title_line_2_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='main_title_line_2_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='our_team_title_en',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='our_team_title_uk',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='related_prod_title_en',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='related_prod_title_uk',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='shop_title_line_1_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='shop_title_line_1_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='shop_title_line_2_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='shop_title_line_2_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uk',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uk',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='promo',
            name='description_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='promo',
            name='description_uk',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='promo',
            name='promo_product_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
        migrations.AddField(
            model_name='promo',
            name='promo_product_uk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
        migrations.AddField(
            model_name='promo',
            name='title_en',
            field=models.CharField(db_index=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='promo',
            name='title_uk',
            field=models.CharField(db_index=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='promo',
            name='type_en',
            field=models.CharField(choices=[('month', 'month'), ('week', 'week'), ('day', 'day')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='promo',
            name='type_uk',
            field=models.CharField(choices=[('month', 'month'), ('week', 'week'), ('day', 'day')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='name_en',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='name_uk',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='profession_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='profession_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='review_en',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='review_uk',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='delivery_text_en',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='delivery_text_uk',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='delivery_title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='delivery_title_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='price_text_en',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='price_text_uk',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='price_title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='price_title_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='refund_text_en',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='refund_text_uk',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='refund_title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='refund_title_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='service_text_en',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='service_text_uk',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='service_title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='service_title_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='contact',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='open_hours',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='text',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
    ]
