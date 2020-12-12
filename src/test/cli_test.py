from click.testing import CliRunner
from cli import cli

def test_cli():
    runner = CliRunner()
    
    # argument missing
    result = runner.invoke(cli, ['command1'])
    assert result.exit_code == 2

    result = runner.invoke(cli, ['command1', 'arg1'])
    assert result.exit_code == 0