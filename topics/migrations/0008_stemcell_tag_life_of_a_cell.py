from django.db import migrations


def tag_stemcell_life_of_a_cell(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Article.objects.filter(slug="stem-cells-how-they-arise").update(
        ai_summary=(
            "Life of a cell — stem cell biology (hematopoietic, skeletal, neural), "
            "Mukherjee's discovery of skeletal stem cells, and the full technology "
            "stack: bone marrow transplant, cord blood, CRISPR/VOR platform, "
            "base editing, CAR-T + edited graft, iPSC reprogramming."
        )
    )


def reverse_tag(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0007_mental_illness_stories"),
    ]

    operations = [
        migrations.RunPython(tag_stemcell_life_of_a_cell, reverse_tag),
    ]
