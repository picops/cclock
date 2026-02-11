Install
=======

With uv (recommended):

.. code-block:: bash

   uv add cclock

With pip:

.. code-block:: bash

   pip install cclock

Requirements: Python >= 3.13.

Build from source (C extensions + Cython):

.. code-block:: bash

   uv sync --extra dev
   uv pip install -e .
