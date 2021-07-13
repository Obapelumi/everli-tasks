<?php

class Path
{
  public $path = '';

  public function __construct($path)
  {
    // set initial path
    $this->cd($path);
  }

  public function cd($newPath)
  {
    // if an absolute path is specified override the previous path
    if ($newPath[0] === '/') {
      return $this->path = $newPath;
    }

    // handle navigation to parent directory
    if (strpos($newPath, '../') === 0) {
      // remove the last folder in path
      $folders = explode('/', $this->path);
      array_pop($folders);
      $this->path = implode('/', $folders);

      // remove the first occurence of ../ in the new path
      $newPath = preg_replace('/../', '', $newPath, 1);
      $newPath = substr($newPath, 1);

      // call the cd fucntion again
      $this->cd($newPath);
    } else {
      $this->path .= '/' . $newPath;
    }
  }
}

// test function - php change_directory.php
$path = new Path('a/b/c');
$path->cd('../../../x/c');
echo $path->path;
