[![CodeQL](https://github.com/nacifyas/posts-demo/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/nacifyas/posts-demo/actions/workflows/codeql-analysis.yml)

Microservice corresponding to manager posts.

Follow the correspondig steps at the API [Gateway Microservice](https://github.com/nacifyas/gateway-edm-demo/) to install and use.

The functionality of this MS is to exclusivly handle *posts* and its CRUD related operations.

This MS uses redis as its primary database, and its event stream for events sourcing.
