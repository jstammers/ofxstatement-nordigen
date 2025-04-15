~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ofxstatement-nordigen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A plugin for `ofxstatement`_ to parse transaction data from GoCardless (previously known as Nordigen).

`ofxstatement`_ is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash. Plugin for ofxstatement parses a
particular proprietary bank statement format and produces common data
structure, that is then formatted into an OFX file.

.. _ofxstatement: https://github.com/kedder/ofxstatement


Installation
================

To install the plugin, you can use `pip`_:

.. _pip: https://pypi.org/project/pip/

.. code-block:: shell

    pip install ofxstatement-nordigen

or, if you want to install it in editable mode (for development), use:

.. code-block:: shell

    pip install -e ./

To verify that the plugin is installed correctly, you can run:

.. code-block:: shell

    ofxstatement --list-plugins

This should list the `nordigen` plugin among other plugins.

Usage
================

To use the plugin, you can run the `ofxstatement` command with the `--plugin` option:

.. code-block:: shell

    ofxstatement convert -t nordigen <input_file> <output_file>

Replace `<input_file>` with the path to your input file and `<output_file>` with the desired output file name.

The input file should be a JSON of transactions from GoCardless that has the schema defined `here`_.

.. _here: https://developer.gocardless.com/bank-account-data/transactions

The output file will be an OFX file that can be imported into GnuCash or other financial software.

After you are done
==================

After your plugin is ready, feel free to open an issue on `ofxstatement`_
project to include your plugin in "known plugin list". That would hopefully
make life of other clients of your bank easier.
