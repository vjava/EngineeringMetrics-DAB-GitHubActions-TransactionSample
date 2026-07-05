resource "databricks_schema" "landing" {
  catalog_name = var.catalog_name
  name = "landing"
}

resource "databricks_volume" "transactions" {
  catalog_name = var.catalog_name
  schema_name = databricks_schema.landing.name
  name = "transactions"
  volume_type = "MANAGED"
}
