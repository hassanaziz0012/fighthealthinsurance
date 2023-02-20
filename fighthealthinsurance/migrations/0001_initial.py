# Generated by Django 4.1.6 on 2023-02-20 00:02

from django.db import migrations, models
import django.db.models.deletion
import regex_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataSource",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Denial",
            fields=[
                ("denial_id", models.AutoField(primary_key=True, serialize=False)),
                ("hashed_email", models.CharField(max_length=300)),
                ("denial_text", models.CharField(max_length=30000000)),
                ("submissions", models.DateField()),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="DenialTypes",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=300)),
                ("regex", regex_field.fields.RegexField(max_length=400)),
                ("negative_regex", regex_field.fields.RegexField(max_length=400)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="fighthealthinsurance.denialtypes",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FollowUpType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("subject", models.CharField(max_length=300)),
                ("text", models.CharField(max_length=30000)),
                ("duration", models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name="PlanType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=300)),
                ("alt_name", models.CharField(max_length=300)),
                ("regex", regex_field.fields.RegexField(max_length=400)),
                ("negative_regex", regex_field.fields.RegexField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name="Regulator",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=300)),
                ("website", models.CharField(max_length=300)),
                ("alt_name", models.CharField(max_length=300)),
                ("regex", regex_field.fields.RegexField(max_length=400)),
                ("negative_regex", regex_field.fields.RegexField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name="FollowUpSched",
            fields=[
                ("follow_up_id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.CharField(max_length=300)),
                ("follow_up_date", models.DateField()),
                ("initial", models.DateField(auto_now_add=True)),
                (
                    "denial_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fighthealthinsurance.denial",
                    ),
                ),
                (
                    "follow_up_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fighthealthinsurance.followuptype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DenialTypesRelation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "denial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fighthealthinsurance.denial",
                    ),
                ),
                (
                    "denial_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fighthealthinsurance.denialtypes",
                    ),
                ),
                (
                    "src",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="fighthealthinsurance.datasource",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DenialRegulatorRelation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "denial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fighthealthinsurance.denial",
                    ),
                ),
                (
                    "regulator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fighthealthinsurance.regulator",
                    ),
                ),
                (
                    "src",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="fighthealthinsurance.datasource",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="denial",
            name="denial_type",
            field=models.ManyToManyField(
                through="fighthealthinsurance.DenialTypesRelation",
                to="fighthealthinsurance.denialtypes",
            ),
        ),
        migrations.AddField(
            model_name="denial",
            name="regulator",
            field=models.ManyToManyField(
                through="fighthealthinsurance.DenialRegulatorRelation",
                to="fighthealthinsurance.regulator",
            ),
        ),
    ]
