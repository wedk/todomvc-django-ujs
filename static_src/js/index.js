// js/index.js
$(function() {

  function enterEditMode() {
    var self = $(this);
    self.addClass('editing');
    setTimeout(function() {
      self.find('input.edit').focus();
    }, 13);
  }

  function exitEditMode(el) {
    el.parents('.editing').removeClass('editing');
  }

  $('.todoapp')
    // edit project title and todo items on double click
    .on('dblclick', 'h1, .todo-list li', enterEditMode)
    .on('keydown', 'input.edit', function(ev) {
      if (ev.keyCode === 27) { // ESCAPE
        var el = $(this);
        el.val(el.attr('data-original-value')); // reset to its original value
        exitEditMode(el);
      } else if (ev.keyCode === 13) { // ENTER
        $(this).blur(); // force blur to submit the form
      }
    })
    .on('blur', 'input.edit', function() {
      var el = $(this);
      if (el.val() === el.attr('data-original-value')) { // no changes
        exitEditMode(el);
      } else { // submit the form
        el.parents('form').submit();
      }
    });

});