"""pathinfo.py:  Object to represent a snapshot of a file's status.

  For documentation in "literate programming" style, see:
    http://www.nmt.edu/help/lang/python/examples/pathinfo/
"""
#================================================================
# Imports
#----------------------------------------------------------------

import os, stat, time
#================================================================
# Manifest constants
#----------------------------------------------------------------

TIME_FORMAT  =  "%Y-%m-%d %H:%M:%S"
#================================================================
# Functions and classes
#----------------------------------------------------------------


# - - - - -   c l a s s   P a t h I n f o   - - - - -

class PathInfo:
    """Represents a snapshot of one file's status.

      Class invariants:
        .path:
          [ the pathname passed to the class constructor ]
        .size:
          [ self.path's size in bytes as an integer ]
        .createEpoch:
          [ the epoch time when self.path was created ]
        .modEpoch:
          [ the epoch time when self.path was last modified ]
        .mode:
          [ the mode bits for self.path ]
"""
# - - -   P a t h I n f o . _ _ i n i t _ _   - - -

    def __init__ ( self, path ):
        """Constructor for the PathInfo class.

          [ path is a string ->
              if path names an inode whose status is readable ->
                return a new PathInfo containing that status
              else -> raise OSError ]
        """
        #-- 1 --
        self.path  =  path
        self.filename  =  os.path.basename(path)
        #-- 2 --
        # [ if path names an existing, accessible file path ->
        #     self.status  :=  the status tuple for path
        #   else -> raise OSError ]
        self.status  =  os.lstat ( path )
        #-- 3 --
        # [ self.status is a status tuple ->
        #     self.size         :=  size from self.status
        #     self.createEpoch  :=  creation epoch time from
        #                           self.status
        #     self.modEpoch     :=  modification epoch time
        #                           from self.status
        #     self.mode         :=  mode bits from self.status ]
        self.size         =  self.status[stat.ST_SIZE]
        self.createEpoch  =  self.status[stat.ST_CTIME]
        self.modEpoch     =  self.status[stat.ST_MTIME]
        self.mode         =  self.status[stat.ST_MODE]
# - - -   P a t h I n f o . i s F i l e   - - -

    def isFile ( self ):
        """Predicate to test whether this path is an ordinary file.

          [ if self represents an ordinary file ->
              return a true value
            else ->
              return a false value ]
        """
        return  stat.S_ISREG ( self.mode )
# - - -   P a t h I n f o . i s D i r   - - -

    def isDir ( self ):
        """Predicate to test whether this path is a directory.

          [ if self represents a directory ->
              return a true value
            else ->
              return a false value ]
        """
        return  stat.S_ISDIR ( self.mode )
# - - -   P a t h I n f o . i s D i r   - - -

    def isLink ( self ):
        """Predicate to test whether this path is a soft link.

          [ if self represents a soft link ->
              return a true value
            else ->
              return a false value ]
        """
        return  stat.S_ISLNK ( self.mode )
# - - -   P a t h I n f o . a b s P a t h   - - -

    def absPath ( self ):
        """Return self's absolute path name."""
        return  os.path.abspath ( self.path )
# - - -   P a t h I n f o . r e a l P a t h   - - -

    def realPath ( self ):
        """Return self's absolute path name, with links resolved."""
        return  os.path.realpath ( self.path )
# - - -  P a t h I n f o . { o w n e r } C a n { R e a d   } - - -
#                          { g r o u p }       { W r i t e }
#                          { w o r l d }       { E x e c   }

    def ownerCanRead ( self ):
        return self.mode & stat.S_IRUSR
    def ownerCanWrite ( self ):
        return self.mode & stat.S_IWUSR

    def ownerCanExec ( self ):
        return self.mode & stat.S_IXUSR

    def groupCanRead ( self ):
        return self.mode & stat.S_IRGRP

    def groupCanWrite ( self ):
        return self.mode & stat.S_IWGRP

    def groupCanExec ( self ):
        return self.mode & stat.S_IXGRP

    def worldCanRead ( self ):
        return self.mode & stat.S_IROTH

    def worldCanWrite ( self ):
        return self.mode & stat.S_IWOTH

    def worldCanExec ( self ):
        return self.mode & stat.S_IXOTH
# - - -   m o d T i m e   - - -

    def modTime ( self ):
        """Format the modification time as yyyy-mm-dd hh:mm:ss."""
        return time.strftime ( TIME_FORMAT,
            time.localtime ( self.modEpoch ) )
# - - -   P a t h I n f o . _ _ s t r _ _   - - -

    def __str__ ( self ):
        """Convert self to a string."""
        return ( "%s%s %s %8d %s" %
                 (self.__fileType(), self.__permFlags(),
                  self.modTime(), self.size, self.path) )
# - - -   P a t h I n f o . _ _ f i l e T y p e   - - -

    def __fileType ( self ):
        """Return the file type code.

          [ if self is a regular file ->
              return "-"
            if self is a directory ->
              return "d"
            if self is a soft link ->
              return "l" ]
        """
        if self.isLink():
            return "l"
        elif self.isDir():
            return "d"
        elif self.isFile():
            return "-"
        else:
            return "?"
# - - -   P a t h I n f o . _ _ p e r m F l a g s   - - -

    def __permFlags ( self ):
        """Format self.mode's permissions as 'rwxrwxrwx'.
        """
        return ( "%s%s%s" %
                 (self.__rwx ( self.mode & stat.S_IRUSR,
                               self.mode & stat.S_IWUSR,
                               self.mode & stat.S_IXUSR ),
                  self.__rwx ( self.mode & stat.S_IRGRP,
                               self.mode & stat.S_IWGRP,
                               self.mode & stat.S_IXGRP ),
                  self.__rwx ( self.mode & stat.S_IROTH,
                               self.mode & stat.S_IWOTH,
                               self.mode & stat.S_IXOTH ) ) )
# - - -   P a t h I n f o . _ _ r w x   - - -

    def __rwx ( self, r, w, x ):
        """Format three permission bits.

          [ r, w, and x are Boolean values indicating read,
            write and execute permissions ->
              return a three-character string displaying those
              permissions as "ls -l" displays them ]
        """
        return  ( "%s%s%s" %
                  (self.__dasher ( r, "r" ),
                   self.__dasher ( w, "w" ),
                   self.__dasher ( x, "x" ) ) )
# - - -   P a t h I n f o . _ _ d a s h e r   - - -

    def __dasher ( self, bit, flag ):
        """Format a permission bit as in ls -l.

          [ (bit is a Boolean value) and (flag is a string) ->
              if bit is true ->
                return flag
              else -> return "-" ]
        """
        if  bit:  return flag
        else:     return "-"
# - - -   P a t h I n f o . _ _ c m p _ _   - - -

    def __cmp__ ( self, other ):
        """Comparison operator for PathInfo objects.

          [ other is a PathInfo object ->
              if self.path < other.path ->
                return a negative number
              else if self.path > other.path ->
                return a positive number
              else ->
                return 0 ]
        """
        return cmp ( self.path, other.path )

