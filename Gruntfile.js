// Gruntfile.js
module.exports = function(grunt) {

  // project configuration
  grunt.initConfig({

    uglify: {
      build: {
        options: {
          mangle: false,
          beautify: true
        },
        files: {
          'static/js.js': [
            'bower_components/jquery-ujs/src/rails.js',
            'static_src/js/django_jquery_ujs_compatibility.js',
            'static_src/js/index.js'
          ]
        }
      },
      dist: {
        mangle: {
          except: ['jQuery']
        },
        files: {
          'static/js.js': [
            'bower_components/jquery-ujs/src/rails.js',
            'static_src/js/django_jquery_ujs_compatibility.js',
            'static_src/js/index.js'
          ]
        }
      }
    },

    clean: {
      css: ['static/css.css', 'static/css.css.map', 'static/todomvc-app-css'],
      js:  ['static/js.js']
    },

    copy: {
      css_todomvc: {
        src: 'node_modules/todomvc-app-css/index.css',
        dest: 'static/todomvc-app-css/index.css'
      }
    },

    'bower-install-simple': {
      build: {}
    },

    sass: {
      build: {
        options: {
          sourcemap: 'auto',
          style: 'expanded'
        },
        files: {
          './static/css.css': './static_src/css/index.scss'
        }
      },
      dist: {
        options: {
          sourcemap: 'none',
          style: 'compressed'
        },
        files: {
          './static/css.css': './static_src/css/index.scss',
          './static/todomvc-app-css/index.css': './static/todomvc-app-css/index.css'
        }
      }
    },

    watch: {
      js: {
        files: ['./static_src/js/**/*'],
        tasks: ['js:build']
      },
      css: {
        files: ['./static_src/css/**/*'],
        tasks: ['css:build']
      }
    }

  });

  // plugins
  grunt.loadNpmTasks('grunt-bower-install-simple');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // - cleaning
  grunt.registerTask('clean:all',  ['clean:js', 'clean:css']);

  // - JS tasks
  grunt.registerTask('js:build',   ['clean:js', 'bower-install-simple', 'uglify:build']);
  grunt.registerTask('js:dist',    ['clean:js', 'bower-install-simple', 'uglify:dist' ]);
  grunt.registerTask('js',         ['js:build']);

  // - CSS/SASS tasks
  grunt.registerTask('css:build',  ['clean:css', 'copy:css_todomvc', 'sass:build']);
  grunt.registerTask('css:dist',   ['clean:css', 'copy:css_todomvc', 'sass:dist' ]);
  grunt.registerTask('css',        ['css:build']);

  // - build (for development environment)
  grunt.registerTask('build',      ['js:build', 'css:build']);

  // - dist (for production environment)
  grunt.registerTask('dist',       ['js:dist', 'css:dist']);

  // - default task
  grunt.registerTask('default',    ['build', 'watch']);

};