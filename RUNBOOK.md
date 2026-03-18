# Runbook — Deployment & Operations

This runbook captures the deployment strategy for this project and provides steps for troubleshooting, deploying, and rolling back in production.

---

## 🚀 Deployment Strategy (GitHub Actions + AWS ECR + Self-hosted)

This repository uses **GitHub Actions** to implement a simple CI/CD pipeline:

1. **Continuous Integration** (`integration` job)
   - Runs on every push to `master`.
   - Lints and runs unit tests (currently placeholders).

2. **Continuous Delivery** (`build-and-push-ecr-image` job)
   - Builds a Docker image from the repository.
   - Pushes the image to **Amazon ECR** using the `latest` tag.

3. **Continuous Deployment** (`Continuous-Deployment` job)
   - Runs on a **self-hosted runner** (typically an EC2 instance or similar).
   - Pulls the `latest` image from ECR.
   - Stops and removes the existing container.
   - Starts a new container exposing port `8080`.


## ✅ Required Secrets (GitHub Repository Settings)

The workflow expects the following secrets to be configured in the repository:

- `AWS_ACCESS_KEY_ID` (used in CI/CD jobs)
- `AWS_SECRET_ACCESS_KEY` (used in CI/CD jobs)
- `AWS_REGION` (e.g., `us-east-1`)
- `ECR_REPOSITORY_NAME` (ECR repo name, e.g. `student-performance`)

> Note: The deployment job assumes the self-hosted runner has an IAM role attached with permissions to access ECR and run Docker.


## 🛠️ Self-Hosted Runner Requirements

The self-hosted runner (e.g., EC2) must have:

- Docker installed and running
- Network access to ECR (internet or VPC endpoints)
- Permissions to pull images from the configured ECR repository
- Sufficient disk space (the workflow runs `docker system prune -af` to reclaim space)


## ✅ Manual Deploy (Triggering the Workflow)

You can manually trigger the pipeline from **GitHub Actions > workflow_dispatch** (the workflow is named `workflow`).


## 🧪 Verifying Deployment

### 1) Check GitHub Actions logs

- Go to **Actions** tab → select the latest run → review logs for each job.

### 2) Verify the running container (on the self-hosted runner)

SSH into the runner and run:

```sh
docker ps
```

Look for the container named `student-performance-ecr`.

### 3) Confirm the service is serving

By default, the container is exposed on **port 8080**. Visit:

```
http://<runner-host>:8080
```


## 🧯 Rollback Procedure

If the latest image causes issues, you can roll back by running a previous image tag from ECR.

1) List available images:

```sh
docker images $ECR_REPOSITORY_NAME --format "{{.Repository}}:{{.Tag}}"
```

2) Update the deployment step to use a known-good tag (e.g., `v1.0.0`) instead of `latest`, then rerun the workflow.

3) Alternatively, on the self-hosted runner:

```sh
docker stop student-performance-ecr || true
docker rm student-performance-ecr || true
docker run -d -p 8080:8080 --name student-performance-ecr <registry>/<repo>:<good-tag>
```


## 🧩 Common Issues

- **Workflow fails due to missing secrets:** Verify all required secrets are set under **Settings → Secrets and variables → Actions**.
- **Docker pull fails:** Ensure the self-hosted runner has access to ECR and the IAM role/credentials are valid.
- **Port 8080 already in use:** Either stop the conflicting process or modify the workflow/container port mapping.

---

## 📌 Notes

- This runbook is tied to the current GitHub Actions workflow at `.github/workflows/aws.yml`.
- If the deployment strategy changes (e.g., using ECS, Lambda, or Kubernetes), update this runbook accordingly.
