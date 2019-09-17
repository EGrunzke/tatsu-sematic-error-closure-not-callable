# tatsu-sematic-error-closure-not-callable
Reproduction of tatsu SemanticError: Could not call constructor: 'closure' object is not callable

## Setup
* `pipenv install`
* `pipenv shell`
* `python -m tatsu bug.peg -o gen/bug_parser.py -G gen/bug_model.py` _(Optional: regenerates parser and model)_

## Reproduction
`python bug.py`

Raises

```
Traceback (most recent call last):
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\semantics.py", line 92, in _default
    return constructor(*args[1:], ast=ast, ctx=self.ctx, **kwargs)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\objectmodel.py", line 34, in __init__
    self._adopt_children(attributes)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\objectmodel.py", line 161, in _adopt_children
    self._adopt_children(c, parent=parent)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\objectmodel.py", line 164, in _adopt_children
    self._adopt_children(c, parent=parent)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\objectmodel.py", line 157, in _adopt_children
    for c in node.children():
TypeError: 'closure' object is not callable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "bug.py", line 20, in <module>
    parser.parse(text, semantics=semantics)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 218, in parse
    result = rule()
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 56, in wrapper
    return self._call(ruleinfo)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 519, in _call
    result = self._recursive_call(ruleinfo)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 548, in _recursive_call
    return self._invoke_rule(ruleinfo, self.memokey)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 595, in _invoke_rule
    ruleinfo.impl(self)
  File "C:\dev\pyspace\tatsu-sematic-error-closure-not-callable\gen\bug_parser.py", line 85, in _start_
    self._sequence_()
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 56, in wrapper
    return self._call(ruleinfo)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 519, in _call
    result = self._recursive_call(ruleinfo)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 548, in _recursive_call
    return self._invoke_rule(ruleinfo, self.memokey)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 597, in _invoke_rule
    node = self._invoke_semantic_rule(ruleinfo, node)
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\contexts.py", line 623, in _invoke_semantic_rule
    node = semantic_rule(node, *(rule.params or ()), **(rule.kwparams or {}))
  File "C:\Users\Grunzkes\.virtualenvs\lugram-me9bNFxp\lib\site-packages\tatsu\semantics.py", line 98, in _default
    % (typename, str(e))
tatsu.exceptions.SemanticError: Could not call constructor for Sequence: 'closure' object is not callable
```