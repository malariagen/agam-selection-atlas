(function() {
  var fn = function() {
    
    (function(root) {
      function now() {
        return new Date();
      }
    
      var force = false;
    
      if (typeof (root._bokeh_onload_callbacks) === "undefined" || force === true) {
        root._bokeh_onload_callbacks = [];
        root._bokeh_is_loading = undefined;
      }
    
      
      
    
      
      
    
      function run_callbacks() {
        try {
          root._bokeh_onload_callbacks.forEach(function(callback) { callback() });
        }
        finally {
          delete root._bokeh_onload_callbacks
        }
        console.info("Bokeh: all callbacks have finished");
      }
    
      function load_libs(js_urls, callback) {
        root._bokeh_onload_callbacks.push(callback);
        if (root._bokeh_is_loading > 0) {
          console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
          return null;
        }
        if (js_urls == null || js_urls.length === 0) {
          run_callbacks();
          return null;
        }
        console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
        root._bokeh_is_loading = js_urls.length;
        for (var i = 0; i < js_urls.length; i++) {
          var url = js_urls[i];
          var s = document.createElement('script');
          s.src = url;
          s.async = false;
          s.onreadystatechange = s.onload = function() {
            root._bokeh_is_loading--;
            if (root._bokeh_is_loading === 0) {
              console.log("Bokeh: all BokehJS libraries loaded");
              run_callbacks()
            }
          };
          s.onerror = function() {
            console.warn("failed to load library " + url);
          };
          console.log("Bokeh: injecting script tag for BokehJS library: ", url);
          document.getElementsByTagName("head")[0].appendChild(s);
        }
      };var element = document.getElementById("0dd365cf-0048-47fe-961b-b78282bb488e");
      if (element == null) {
        console.log("Bokeh: ERROR: autoload.js configured with elementid '0dd365cf-0048-47fe-961b-b78282bb488e' but no matching script tag was found. ")
        return false;
      }
    
      var js_urls = ["https://cdn.pydata.org/bokeh/release/bokeh-0.12.13.min.js", "https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.13.min.js", "https://cdn.pydata.org/bokeh/release/bokeh-tables-0.12.13.min.js", "https://cdn.pydata.org/bokeh/release/bokeh-gl-0.12.13.min.js"];
    
      var inline_js = [
        function(Bokeh) {
          Bokeh.set_log_level("info");
        },
        
        function(Bokeh) {
          
        },
        
        function(Bokeh) {
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json = '{"b5897bc3-3c5b-4aaa-a51e-b2455d6b40ea":{"roots":{"references":[{"attributes":{"formatter":{"id":"bad59eb2-9ad6-41c4-ac1b-82e07996562e","type":"BasicTickFormatter"},"plot":{"id":"2b8f6778-0025-4980-b0e4-eb02b667ac9f","subtype":"Figure","type":"Plot"},"ticker":{"id":"9b612597-1047-4682-99b6-d487c1a85363","type":"BasicTicker"}},"id":"499c38f2-25f3-4a1e-89a8-ebe7c00833d6","type":"LinearAxis"},{"attributes":{"plot":null,"text":"example"},"id":"013a25ac-5451-49e5-981f-1b8571d68383","type":"Title"},{"attributes":{},"id":"4f69095d-2721-47ff-ba61-4abc7434d3e1","type":"LinearScale"},{"attributes":{"source":{"id":"f657e94f-ee1a-4098-a84a-e696b6f64978","type":"ColumnDataSource"}},"id":"ad2d01c6-18a1-4b33-b02c-908a54d5755b","type":"CDSView"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"76f2df6b-c408-4288-a553-4cfea9ad9724","type":"BoxAnnotation"},{"attributes":{},"id":"a90cf96e-9464-4b1a-bf36-e3314d7e7cb8","type":"PanTool"},{"attributes":{"callback":null},"id":"2d2c4946-04e7-4519-862e-e566b8c3a5b4","type":"DataRange1d"},{"attributes":{},"id":"c4d345bb-9abd-487d-b807-712eb4d6d93f","type":"WheelZoomTool"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"a90cf96e-9464-4b1a-bf36-e3314d7e7cb8","type":"PanTool"},{"id":"c4d345bb-9abd-487d-b807-712eb4d6d93f","type":"WheelZoomTool"},{"id":"103481d3-2a69-4c78-a783-79644e981848","type":"BoxZoomTool"},{"id":"3976328c-9627-4c9a-b400-313b6942c9a7","type":"SaveTool"},{"id":"ffe33447-1dc5-4e2e-9ad8-994e8195676d","type":"ResetTool"},{"id":"24c0a194-9bdd-4243-bd93-e65ba00d39a8","type":"HelpTool"}]},"id":"d88286fa-9a41-49c4-818e-02e83455f244","type":"Toolbar"},{"attributes":{"overlay":{"id":"76f2df6b-c408-4288-a553-4cfea9ad9724","type":"BoxAnnotation"}},"id":"103481d3-2a69-4c78-a783-79644e981848","type":"BoxZoomTool"},{"attributes":{"callback":null},"id":"3dddb759-7e39-4f83-904c-2488d8ac9b88","type":"DataRange1d"},{"attributes":{},"id":"3976328c-9627-4c9a-b400-313b6942c9a7","type":"SaveTool"},{"attributes":{"data_source":{"id":"f657e94f-ee1a-4098-a84a-e696b6f64978","type":"ColumnDataSource"},"glyph":{"id":"893948f3-229a-48fc-abba-1db210616b7f","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"e9f801ea-4080-490b-87b1-9f47b13247c1","type":"Line"},"selection_glyph":null,"view":{"id":"ad2d01c6-18a1-4b33-b02c-908a54d5755b","type":"CDSView"}},"id":"ab4b70dd-08ba-41b2-a6d7-e8a85830f455","type":"GlyphRenderer"},{"attributes":{},"id":"ffe33447-1dc5-4e2e-9ad8-994e8195676d","type":"ResetTool"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":2,"x":{"field":"x"},"y":{"field":"y"}},"id":"e9f801ea-4080-490b-87b1-9f47b13247c1","type":"Line"},{"attributes":{},"id":"24c0a194-9bdd-4243-bd93-e65ba00d39a8","type":"HelpTool"},{"attributes":{"callback":null,"column_names":["x","y"],"data":{"x":[1,2,3,4,5],"y":[6,7,6,4,5]}},"id":"6f5cb6c9-1e3a-4514-87e4-aa6610261227","type":"ColumnDataSource"},{"attributes":{"line_color":"#1f77b4","line_width":2,"x":{"field":"x"},"y":{"field":"y"}},"id":"893948f3-229a-48fc-abba-1db210616b7f","type":"Line"},{"attributes":{"data_source":{"id":"6f5cb6c9-1e3a-4514-87e4-aa6610261227","type":"ColumnDataSource"},"glyph":{"id":"bd0f812f-4cf9-4cdf-8504-d1c9c98cddee","type":"Circle"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"3673a47b-c9df-41c5-9bb1-5066b74b43b5","type":"Circle"},"selection_glyph":null,"view":{"id":"682ca732-40e5-47ca-b1df-e351c3351739","type":"CDSView"}},"id":"89948669-8b5d-4c1d-bd79-b9b527727160","type":"GlyphRenderer"},{"attributes":{"fill_color":{"value":"white"},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"bd0f812f-4cf9-4cdf-8504-d1c9c98cddee","type":"Circle"},{"attributes":{"source":{"id":"6f5cb6c9-1e3a-4514-87e4-aa6610261227","type":"ColumnDataSource"}},"id":"682ca732-40e5-47ca-b1df-e351c3351739","type":"CDSView"},{"attributes":{},"id":"28b40623-c15d-46df-beeb-b2a4212ae45d","type":"LinearScale"},{"attributes":{},"id":"bad59eb2-9ad6-41c4-ac1b-82e07996562e","type":"BasicTickFormatter"},{"attributes":{},"id":"01f64642-cf17-4980-8a41-68bc9dab0bff","type":"BasicTickFormatter"},{"attributes":{"callback":null,"column_names":["x","y"],"data":{"x":[1,2,3,4,5],"y":[6,7,6,4,5]}},"id":"f657e94f-ee1a-4098-a84a-e696b6f64978","type":"ColumnDataSource"},{"attributes":{},"id":"446bc51a-dc42-4f59-b621-e49e6d886e82","type":"BasicTicker"},{"attributes":{"below":[{"id":"499c38f2-25f3-4a1e-89a8-ebe7c00833d6","type":"LinearAxis"}],"left":[{"id":"dce90818-4792-4818-96ff-734c5004f2d2","type":"LinearAxis"}],"plot_height":300,"plot_width":300,"renderers":[{"id":"499c38f2-25f3-4a1e-89a8-ebe7c00833d6","type":"LinearAxis"},{"id":"82e94dcb-9956-43d6-b7d3-fb68f4bffd3c","type":"Grid"},{"id":"dce90818-4792-4818-96ff-734c5004f2d2","type":"LinearAxis"},{"id":"2441e2f6-0ef6-49a5-96e3-8b4703964032","type":"Grid"},{"id":"76f2df6b-c408-4288-a553-4cfea9ad9724","type":"BoxAnnotation"},{"id":"ab4b70dd-08ba-41b2-a6d7-e8a85830f455","type":"GlyphRenderer"},{"id":"89948669-8b5d-4c1d-bd79-b9b527727160","type":"GlyphRenderer"}],"title":{"id":"013a25ac-5451-49e5-981f-1b8571d68383","type":"Title"},"toolbar":{"id":"d88286fa-9a41-49c4-818e-02e83455f244","type":"Toolbar"},"x_range":{"id":"3dddb759-7e39-4f83-904c-2488d8ac9b88","type":"DataRange1d"},"x_scale":{"id":"28b40623-c15d-46df-beeb-b2a4212ae45d","type":"LinearScale"},"y_range":{"id":"2d2c4946-04e7-4519-862e-e566b8c3a5b4","type":"DataRange1d"},"y_scale":{"id":"4f69095d-2721-47ff-ba61-4abc7434d3e1","type":"LinearScale"}},"id":"2b8f6778-0025-4980-b0e4-eb02b667ac9f","subtype":"Figure","type":"Plot"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"3673a47b-c9df-41c5-9bb1-5066b74b43b5","type":"Circle"},{"attributes":{"dimension":1,"plot":{"id":"2b8f6778-0025-4980-b0e4-eb02b667ac9f","subtype":"Figure","type":"Plot"},"ticker":{"id":"446bc51a-dc42-4f59-b621-e49e6d886e82","type":"BasicTicker"}},"id":"2441e2f6-0ef6-49a5-96e3-8b4703964032","type":"Grid"},{"attributes":{"plot":{"id":"2b8f6778-0025-4980-b0e4-eb02b667ac9f","subtype":"Figure","type":"Plot"},"ticker":{"id":"9b612597-1047-4682-99b6-d487c1a85363","type":"BasicTicker"}},"id":"82e94dcb-9956-43d6-b7d3-fb68f4bffd3c","type":"Grid"},{"attributes":{},"id":"9b612597-1047-4682-99b6-d487c1a85363","type":"BasicTicker"},{"attributes":{"formatter":{"id":"01f64642-cf17-4980-8a41-68bc9dab0bff","type":"BasicTickFormatter"},"plot":{"id":"2b8f6778-0025-4980-b0e4-eb02b667ac9f","subtype":"Figure","type":"Plot"},"ticker":{"id":"446bc51a-dc42-4f59-b621-e49e6d886e82","type":"BasicTicker"}},"id":"dce90818-4792-4818-96ff-734c5004f2d2","type":"LinearAxis"}],"root_ids":["2b8f6778-0025-4980-b0e4-eb02b667ac9f"]},"title":"Bokeh Application","version":"0.12.13"}}';
                  var render_items = [{"docid":"b5897bc3-3c5b-4aaa-a51e-b2455d6b40ea","elementid":"0dd365cf-0048-47fe-961b-b78282bb488e","modelid":"2b8f6778-0025-4980-b0e4-eb02b667ac9f"}];
                  root.Bokeh.embed.embed_items(docs_json, render_items);
                
                  }
                  if (root.Bokeh !== undefined) {
                    embed_document(root);
                  } else {
                    var attempts = 0;
                    var timer = setInterval(function(root) {
                      if (root.Bokeh !== undefined) {
                        embed_document(root);
                        clearInterval(timer);
                      }
                      attempts++;
                      if (attempts > 100) {
                        console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing")
                        clearInterval(timer);
                      }
                    }, 10, root)
                  }
                })(window);
              });
            };
            if (document.readyState != "loading") fn();
            else document.addEventListener("DOMContentLoaded", fn);
          })();
        },
        function(Bokeh) {
          console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-0.12.13.min.css");
          Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-0.12.13.min.css");
          console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.13.min.css");
          Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.13.min.css");
          console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-tables-0.12.13.min.css");
          Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-tables-0.12.13.min.css");
        }
      ];
    
      function run_inline_js() {
        
        for (var i = 0; i < inline_js.length; i++) {
          inline_js[i].call(root, root.Bokeh);
        }
        
      }
    
      if (root._bokeh_is_loading === 0) {
        console.log("Bokeh: BokehJS loaded, going straight to plotting");
        run_inline_js();
      } else {
        load_libs(js_urls, function() {
          console.log("Bokeh: BokehJS plotting callback run at", now());
          run_inline_js();
        });
      }
    }(window));
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();