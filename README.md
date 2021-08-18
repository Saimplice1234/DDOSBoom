# UserAgentProvider

This tool has been created to provide user agents strings quickly.In computing, a user agent is software (a software agent) that is acting on behalf of a user, such as a web browser that "retrieves, renders and facilitates end user interaction with Web content

## Packages used

1. requests
2. sys
3. bs4
4. time
5. subprocess

## Goals

1. Self-hosting my most used services for privacy reasons.
2. Being able to customize my setup and add more features whenever I want.

## Software

### OpenBSD base system:

- acme-client(1): for managing Let's Encrypt certificates.
- httpd(8): nice and simple web server.
- smtpd(8): for managing mails.

### Ports:

- dovecot: for IMAP access.
- Git and cgit: for managing source code repositories.
- PHP: for running RainLoop and Nextcloud.
- PostgreSQL: data storage for Nextcloud.
- rspamd: spam filtering system.

### Web systems:

- RainLoop: a nice UI for the email system.
- Nextcloud: a safe place for all your files.

Please remember to always check the source and not just run some random code on your machine.

## Installation

Just run the following commands as root:

`chmod +x setup.sh && ./setup.sh`

You will be prompt for some basic information required for the configuration files.

## What you will get after installation:

A fully functional self-hosted server for your git repositories, files, and mails.
