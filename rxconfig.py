import reflex as rx

config = rx.Config(
    app_name="proyecto_pa",
    plugins=[rx.plugins.TailwindV3Plugin()],
    db_url = "postgresql://postgres.zeccamfcojwukuzsmdcs:Gusbunbury1707.@aws-0-us-east-2.pooler.supabase.com:6543/postgres"
)