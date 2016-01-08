// js/django_jquery_ujs_compatibility.js

/*
  This script should be included before the unobtrusive scripting adapter for jQuery (jquery-ujs).
*/

$(function() {

  var CSRF_TOKEN_COOKIE_NAME = 'csrftoken'; // default name, cf. CSRF_COOKIE_NAME django setting
  var CSRF_PARAM_NAME        = 'csrfmiddlewaretoken';

  function getCookieValue(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  var csrfToken = getCookieValue(CSRF_TOKEN_COOKIE_NAME);

  $('head').append(
    '<meta name="csrf-param" content="' + CSRF_PARAM_NAME + '">' +
    '<meta name="csrf-token" content="' + csrfToken + '">'
  );

});