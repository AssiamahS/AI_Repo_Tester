import subprocess
import os

def clone_repo(repo_url, repo_dir):
    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)

def run_tests(repo_dir):
    result = subprocess.run(["pytest", repo_dir], capture_output=True, text=True)
    return {
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode
    }

def test_repository(repo_url):
    repo_dir = "/tmp/test_repo"
    try:
        clone_repo(repo_url, repo_dir)
        test_result = run_tests(repo_dir)
        return {
            'status': 'PASS' if test_result['returncode'] == 0 else 'FAIL',
            'details': test_result
        }
    except subprocess.CalledProcessError as e:
        return {
            'status': 'ERROR',
            'details': str(e)
        }
