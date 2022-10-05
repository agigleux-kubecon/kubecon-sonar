resource "azurerm_backup_policy_file_share" "s6364-bpfs-nc1" {
  name                = "s6364-bpfs-nc1"
  resource_group_name = azurerm_resource_group.example.name
  recovery_vault_name = azurerm_recovery_services_vault.vault.name

  timezone = "UTC"

  backup {
    frequency = "Daily"
    time      = "23:00"
  }

  retention_daily {
    count = 2  # Sensitive
  }
}