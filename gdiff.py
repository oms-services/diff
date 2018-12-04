from diff_match_patch import diff_match_patch

class GDiff:
  def __init__(self):
    self.dmp = diff_match_patch()
  
  def _patch(self, t1, t2):
    return self.dmp.patch_make(t1, t2)

  def diff(self, t1, t2):
    patch = self._patch(t1, t2)
    diff = self.dmp.patch_toText(patch)    
    return diff