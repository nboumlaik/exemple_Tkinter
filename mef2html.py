#!/usr/bin/python
""" Program mef2html

INTRODUCTION
------------

mef2html convert a file in a mef format into html.

I have defined the mef format for my own use, to be faster and easiest to write than html.
You don't have to worry with header and footer for example.

You have less things to write and it is easy to add macro.

VERSION & AUTHOR
----------------

version: 1.0 (in python the previous one was written in perl)
date: 14 december 2004
author: Jean-Louis Bicquelet-Salaun
mail: jlbicquelet@free.fr

OS: Dos, Windows 98/200/XP, Unix, Linux

LICENSE
-------

This software is under GNU License

HOW TO USE
----------

You just have to type

mef2html.py file.mef under Dos or Windows operating system
mef2html file.mef under Unix and Linux

MEF FORMAT
----------

SYNTAX

Syntax is either:

  - @cmd/ to open a tag @cmd to close the tag for complex command or command that can be
    cascaded. example:

    @b/ @i/ word @i @b to put word in italic bold

  - @cmd( expression ) for simple command, links, images ...
    example:

    header1      @h1(title)
    link         @link(jlbicquelet@free.fr,mon site)

PREDEFINE SYMBOLS

style format

              open   close
bold           @b/    @b
italic         @i/    @i
underline      @u/    @u
red            @cr/   @cr
green          @cg/   @cg
blue           @cb/   @cb
black          @cn/   @cn
stop color            @c

espace         ___


links, images, header

header1    @h1()    or h1
header2    @h2()    or h2
header3    @h3()    or h3
header4    @h4()    or h4

image      @img()
link       @link(,)

lists

               open   close
numbered list   @lo/   @lo
list            @lu/   @lu
item            @li/   @li
                @-

table

                   open   close  cell
table               @t/     @t
table with border   @t1/    @t

head row            @h/     @h    @+
row                 @r/     @r    @:

EXAMPLE

VERSION 1.2

"""
import getopt,sys
import string
import re
#from meftohtml import *

title=''

def Fileread(filename):
   """
   read a file and put it in the text variable
   """
   try:
     f = open(filename, 'r')
     s = f.readlines()
     f.close()
   except:
      print 'error reading file',filename
      sys.exit(-1)
   return s

def Filewrite(filename, text):
   """
   write a string into a file. Be sure the path exist.
   """
   # at a later date, add code here to create directories
   # if they don't exist
   f = open(filename, 'w')
   f.write(text)
   f.close()

def help():
  """Usage
  """
  print """
usage : mef2html file
  """
  sys.exit()

def man():
  """man page for external documentation"""
  print """
NAME mef2html

SYNOPSIS mef2html file

OPTIONS

-h --help   help
-m --man    man

AUTHOR
  Jean-Louis Bicquelet-Salaun (c) 2004

SEE ALSO
  """
  sys.exit()


def process(filename,output):
  """read the given file, process line by line
  """
  text=Fileread(filename)
  res="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//FR" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr"><head>

  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
  <title>%s</title>

  <meta name="description" content="">
  <meta name="keywords" content="">
  <link rel="shortcut icon" href="">
  <link href="document.css" rel="stylesheet" type="text/css" media="screen" title="style">
</head><body>
  """ % title
# transformed by the library meftohtml for standardisation
  res=res+meftohtml(text)

# footer
  res=res+"""</html>
</body>"""
  Filewrite(output,res)



def main():
  """main part, parse options and do actions
  """

  try:
    opts,args=getopt.getopt(sys.argv[1:],"hmo:v",["help","man","output="])
  except getopt.GetoptError:
    help()
    sys.exit(2)

  verbose = False
  output='mef.html'
  for o,a in opts:
     if o== "-v":
       verbose = True
     if o in ("-h","--help"):
       help()
     if o in ("-m","--man"):
       man()
     if o in ("-o","--output"):
       output = a
     if o in ("-t","--title"):
       title = a

  filelist=sys.argv[-1:]
  process(filelist[0],output)

if __name__ == '__main__':
   main()