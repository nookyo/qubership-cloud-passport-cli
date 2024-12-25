import subprocess

def test_help_command():
    result = subprocess.run(
        ["cloud_passport_cli", "put_label", "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Usage:" in result.stdout
    assert "put_label" in result.stdout