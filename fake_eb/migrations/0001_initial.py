# Generated by Django 2.0 on 2019-11-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeEventbriteEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.TextField(default='Fake Eventbrite Event')),
                ('name_html', models.TextField(default='Fake Eventbrite Event')),
                ('description_text', models.TextField(blank=True, default='Fake Eventbrite Event Description', null=True)),
                ('description_html', models.TextField(blank=True, default='Fake Eventbrite Event Description', null=True)),
                ('eventbrite_id', models.CharField(default='1234567', max_length=20)),
                ('day_specifier', models.TextField()),
                ('offset_specifier', models.TextField()),
                ('duration_specifier', models.TextField()),
                ('organization_id', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('capacity', models.IntegerField()),
                ('capacity_is_custom', models.BooleanField(default=False)),
                ('status', models.TextField(choices=[('draft', 'draft'), ('live', 'live'), ('started', 'started'), ('ended', 'ended'), ('completed', 'completed'), ('canceled', 'canceled')], default='live')),
                ('currency', models.CharField(default='USD', max_length=5)),
                ('listed', models.BooleanField(default=False)),
                ('shareable', models.BooleanField(default=True)),
                ('invite_only', models.BooleanField(default=False)),
                ('password', models.CharField(default='password', max_length=64)),
                ('online_event', models.BooleanField(default=False)),
                ('show_remaining', models.BooleanField(default=True)),
                ('tx_time_limit', models.IntegerField(default=480)),
                ('hide_start_date', models.BooleanField(default=False)),
                ('hide_end_date', models.BooleanField(default=False)),
                ('locale', models.CharField(default='en_US', max_length=10)),
                ('is_locked', models.BooleanField(default=False)),
                ('privacy_setting', models.CharField(default='unlocked', max_length=20)),
                ('is_series', models.BooleanField(default=False)),
                ('is_series_parent', models.BooleanField(default=False)),
                ('is_reserved_seating', models.BooleanField(default=False)),
                ('show_pick_a_seat', models.BooleanField(default=False)),
                ('show_seatmap_thumbnail', models.BooleanField(default=False)),
                ('show_colors_in_seatmap_thumbnail', models.BooleanField(default=False)),
                ('source', models.CharField(default='create_2.0', max_length=20)),
                ('is_free', models.BooleanField(default=False)),
                ('version', models.CharField(default='3.0.0', max_length=20)),
                ('summary', models.TextField(blank=True, null=True)),
                ('logo_id', models.CharField(blank=True, max_length=20, null=True)),
                ('organizer_id', models.CharField(default=1111111, max_length=20)),
                ('venue_id', models.CharField(default='7882563', max_length=20)),
                ('category_id', models.CharField(blank=True, max_length=20, null=True)),
                ('subcategory_id', models.CharField(blank=True, max_length=20, null=True)),
                ('format_id', models.CharField(blank=True, max_length=20, null=True)),
                ('is_externally_ticketed', models.BooleanField(default=False)),
            ],
        ),
    ]
