"""Console script for mampoer."""
import sys
import click
from mampoer import Mampoer


@click.command()
@click.option(
    "-d",
    "--directory",
    default="mampoer_alembic",
    type=click.STRING,
    help="String path of the target directory. default=mampoer_alembic",
)
@click.option(
    "-t",
    "--template",
    default="mampoer_generic",
    type=click.STRING,
    help="Setup template for use with 'init'. default=mampoer_generic",
)
@click.option(
    "-p",
    "--package",
    default=False,
    type=click.BOOL,
    is_flag=True,
    help="Write empty __init__.py files to the environment and version locations.",
)
def init(directory, template, package):
    mampoer = Mampoer()
    mampoer.init(directory=directory, template=template, package=package)


@click.command()
@click.option(
    "-m", "--message", type=click.STRING, help="Message string to use with 'revision'",
)
@click.option(
    "--head",
    default="head",
    type=click.STRING,
    help="Head revision to build the new revision upon as a parent. default=head",
)
@click.option(
    "--splice",
    default=False,
    type=click.BOOL,
    is_flag=True,
    help="Whether or not the new revision should be made into a new head of its own. default=False",
)
@click.option(
    "--branch-label", type=click.STRING, help="String label to apply to the branch",
)
@click.option(
    "--version-path",
    type=click.STRING,
    help="String symbol identifying a specific version path from the configuration",
)
@click.option(
    "--rev-id",
    type=click.STRING,
    help="Optional revision identifier to use instead of having one generated",
)
@click.option(
    "--depends-on", type=click.STRING, help='Optional list of "depends on" identifiers',
)
def revision(
    message=None,
    head="head",
    splice=False,
    branch_label=None,
    version_path=None,
    rev_id=None,
    depends_on=None,
):
    """Create a new revision file.

    :param message: string message to apply to the revision; this is the
     ``-m`` option to ``alembic revision``.

    :param head: head revision to build the new revision upon as a parent;
     this is the ``--head`` option to ``alembic revision``.

    :param splice: whether or not the new revision should be made into a
     new head of its own; is required when the given ``head`` is not itself
     a head.  This is the ``--splice`` option to ``alembic revision``.

    :param branch_label: string label to apply to the branch; this is the
     ``--branch-label`` option to ``alembic revision``.

    :param version_path: string symbol identifying a specific version path
     from the configuration; this is the ``--version-path`` option to
     ``alembic revision``.

    :param rev_id: optional revision identifier to use instead of having
     one generated; this is the ``--rev-id`` option to ``alembic revision``.

    :param depends_on: optional list of "depends on" identifiers; this is the
     ``--depends-on`` option to ``alembic revision``.

      .. versionadded:: 0.9.0

    """

    Mampoer().revision(
        message=message,
        head=head,
        splice=splice,
        branch_label=branch_label,
        version_path=version_path,
        rev_id=rev_id,
        depends_on=depends_on,
    )


@click.command()
@click.option(
    "--revisions", type=click.STRING, help="String message to apply to the revision",
)
@click.option(
    "-m",
    "--message",
    type=click.STRING,
    help="String message to apply to the revision",
)
@click.option(
    "--branch-label",
    type=click.STRING,
    help="String label name to apply to the new revision",
)
@click.option(
    "--rev-id",
    type=click.STRING,
    help="Hardcoded revision identifier instead of generating a new one.",
)
def merge(revisions, message=None, branch_label=None, rev_id=None):
    """Merge two revisions together.  Creates a new migration file.

    .. versionadded:: 0.7.0


    :param message: string message to apply to the revision

    :param branch_label: string label name to apply to the new revision

    :param rev_id: hardcoded revision identifier instead of generating a new
     one.

    .. seealso::

        :ref:`branches`

    """
    Mampoer().merge(
        revisions=revisions, message=message, branch_label=branch_label, rev_id=rev_id,
    )


@click.group()
def main(args=None):
    pass


main.add_command(init)
main.add_command(revision)
main.add_command(merge)

if __name__ == "__main__":
    main()
