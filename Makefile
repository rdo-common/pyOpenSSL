# Makefile for source rpm: pyOpenSSL
# $Id$
NAME := pyOpenSSL
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
