# Generated by Django 5.1.3 on 2024-11-19 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_topic_room_host_mesage_room_topic"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": (["-updated"], ["created"])},
        ),
    ]