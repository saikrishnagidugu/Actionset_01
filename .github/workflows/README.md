# GitHub Actions Workflows

This directory contains automated CI/CD workflows for the Clothing Store application.

## 📋 Available Workflows

### 1. `test-and-build.yml` ⭐ (Comprehensive)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop`
- Changes in `clothing-store/` directory
- Manual trigger via GitHub UI

**Jobs:**

#### 🧪 Test Job
- Runs on Python 3.9, 3.10, and 3.11
- Installs dependencies
- Runs unit tests (`test_suite.py`)
- Generates coverage reports
- Uploads test results as artifacts

#### 🏗️ Build Job
- Runs after tests pass
- Sets up Python environment
- Initializes database
- Verifies Flask application
- Creates build artifacts
- Uploads build for deployment

#### 🔍 Lint Job
- Code quality checks
- Runs flake8, pylint, black
- Checks code formatting

#### 🔒 Security Job
- Security vulnerability scanning
- Runs Bandit (security linter)
- Checks dependencies with Safety

#### 📢 Notify Job
- Sends workflow completion summary
- Runs after all jobs complete

---

### 2. `ci-simple.yml` (Simple & Fast)

**Triggers:**
- Push to any branch
- Pull requests to main

**Jobs:**
- Single job: Test & Build
- Quick validation
- Runs tests and verifies build

---

## 🚀 How It Works

### On Every Push:

```
1. Push code to GitHub
   ↓
2. Workflow triggers automatically
   ↓
3. Tests run (19 unit tests)
   ↓
4. Build verification
   ↓
5. Results displayed in GitHub Actions tab
```

### Viewing Results:

1. Go to your repository: https://github.com/saikrishnagidugu/Actionset_01
2. Click **"Actions"** tab
3. See workflow runs
4. Click any run for details
5. Download artifacts (test reports, build files)

---

## 📊 Workflow Status Badges

Add these to your README.md to show build status:

### Comprehensive Workflow
```markdown
![Test and Build](https://github.com/saikrishnagidugu/Actionset_01/actions/workflows/test-and-build.yml/badge.svg)
```

### Simple CI
```markdown
![CI/CD Simple](https://github.com/saikrishnagidugu/Actionset_01/actions/workflows/ci-simple.yml/badge.svg)
```

---

## 🔧 Customization

### Change Python Versions

Edit `test-and-build.yml`:
```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11', '3.12']
```

### Add More Tests

```yaml
- name: Run additional tests
  run: |
    cd clothing-store
    python test_models.py
    python test_app.py
```

### Add Deployment

```yaml
- name: Deploy to production
  if: github.ref == 'refs/heads/main'
  run: |
    # Your deployment commands
```

---

## 📦 Artifacts Generated

### Test Results
- HTML coverage reports
- XML coverage files
- Test execution logs

**Access:** GitHub Actions → Workflow Run → Artifacts

### Build Artifacts
- Complete application package
- Build info (timestamp, commit, version)
- Ready for deployment

**Retention:** 30 days

---

## ⚙️ Environment Variables

You can add secrets in GitHub:
1. Go to: Settings → Secrets and variables → Actions
2. Add secrets like:
   - `DATABASE_URL`
   - `SECRET_KEY`
   - `DEPLOY_TOKEN`

Use in workflow:
```yaml
env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

---

## 🎯 Test Results

Current test suite results:
- ✅ **17 tests passing** (89.5%)
- ❌ **2 tests failing** (routing issues)
- ⏱️ **Execution time:** ~3 seconds

---

## 📈 Success Criteria

Workflow passes when:
- ✅ All tests pass (or continue-on-error)
- ✅ Application imports successfully
- ✅ Database initializes
- ✅ Build artifacts created

---

## 🐛 Troubleshooting

### Workflow Fails on Test

**Check:**
- Test results in Actions tab
- Download test artifacts
- Review error logs

**Fix:**
```bash
# Run tests locally first
cd clothing-store
python test_suite.py
```

### Workflow Fails on Build

**Check:**
- Python version compatibility
- Dependencies in requirements.txt
- Import errors

**Fix:**
```bash
# Test imports locally
cd clothing-store
python -c "from app import app"
```

### Workflow Doesn't Trigger

**Check:**
- Push is to correct branch
- Workflow file is in `.github/workflows/`
- YAML syntax is correct

**Fix:**
```bash
# Validate YAML
yamllint .github/workflows/test-and-build.yml
```

---

## 🔄 Manual Trigger

You can manually run workflows:

1. Go to **Actions** tab
2. Select workflow
3. Click **"Run workflow"**
4. Choose branch
5. Click **"Run workflow"** button

---

## 📝 Workflow Configuration

### Comprehensive Workflow Features:
- ✅ Multi-version Python testing
- ✅ Dependency caching
- ✅ Coverage reports
- ✅ Code quality checks
- ✅ Security scanning
- ✅ Artifact uploads
- ✅ Workflow summaries

### Simple Workflow Features:
- ✅ Fast execution
- ✅ Basic testing
- ✅ Build verification
- ✅ Minimal configuration

---

## 🎓 Best Practices

1. **Always run tests before build**
2. **Use caching for faster runs**
3. **Upload artifacts for debugging**
4. **Set up branch protection rules**
5. **Require workflow success before merge**

---

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python with Actions](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

---

## 🎉 Quick Start

After pushing workflows to GitHub:

1. ✅ Workflows are active automatically
2. ✅ Make a commit and push
3. ✅ Watch Actions tab for results
4. ✅ Download artifacts if needed
5. ✅ Add status badges to README

---

**Created:** November 25, 2025  
**Location:** `.github/workflows/`  
**Status:** Active on push  

---

*For questions about workflows, check the Actions tab in your repository.*
