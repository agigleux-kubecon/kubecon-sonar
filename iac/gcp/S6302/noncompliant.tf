data "google_iam_policy" "s6302-noncompliant0" {
  binding {
    role = "roles/actions.Admin"  # Sensitive

    members = [
      "user:jane@example.com",
    ]
  }
}

resource "google_project_iam_policy" "s6302-noncompliant1" {
  # Also applies to: google_organization_iam_policy, google_service_account_iam_policy, google_folder_iam_policy

  project     = "appsec-sandbox"
  policy_data = data.google_iam_policy.s6302-noncompliant0.policy_data  # 2nd location
}

resource "google_project_iam_binding" "s6302-noncompliant2" {
  # Also applies to: google_organization_iam_binding, google_service_account_iam_binding, google_folder_iam_binding

  project = "appsec-sandbox"
  role    = "roles/actions.Admin"  # Sensitive

  members = [
    "user:jane@example.com",
  ]
}

resource "google_project_iam_member" "s6302-noncompliant3" {
  # Also applies to: google_organization_iam_member, google_service_account_iam_member, google_folder_iam_member

  project = "appsec-sandbox"
  role    = "roles/actions.Admin"  # Sensitive
  member  = "user:jane@example.com"
}