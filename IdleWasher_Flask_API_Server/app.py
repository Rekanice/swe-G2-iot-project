<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap" rel="stylesheet">
    <style>
        html { 
            zoom: 2; 
        }
        h1 {
            font-family:'Noto Sans',monospace, 'Segoe UI', sans-serif;
        }
        p, div {
            font-family:'Noto Sans', monospace, 'Segoe UI', sans-serif;
            font-size: 13px;
            vertical-align: middle;
        }
        .wm-element-text {
            font-size: 12px;
        }
        .updatetime, .legend {
            font-size: 10px;
        }

    </style>
    
    <title>Idle Washer</title>

    {{ turbo() }}  <!-- Calling this function to initialize the turbo.js library. -->
    
</head>

<body style="background: rgb(245, 245, 245);">
    <div id="bg-flex-container" style="      
        display:flex;
        flex-direction:row;
        justify-content:center;
        align-items: center;
        ">
        <div id="content-flex-container" style="
        display:flex;
        flex-direction:column;
        justify-content:flex-start;
        align-items: flex-start;
        ">
            <div style="
                display: flex;
                justify-content: center;
                align-items: flex-start;">
                <h1>Idle Washing Machines </h1> 
                <div style="
                margin-block-start: 0.67em;
                margin-block-end: 0.67em;
                margin-inline-start: 0px;
                margin-inline-end: 0px;
                font-size: 2em;"> &nbsp;&#129530;</div>
            </div>
            
            <div style="display:flex; flex-direction:column; align-items: flex-start;">
                <p>Location: <code style="    
                    color: #383838;
                    font-size: 10px;
                    font-weight: lighter;
                    border: 0.1px solid #adadad;
                    border-radius: 3px;
                    padding: 0.1rem 0.4rem;"
                    >K10, UB1, GF right wing</code> </p>
                
                {% include 'wm_element.html' %}
                
            </div>
            <br>
            <div >
                <p class="legend"><b>Legend</b></p>
                <p class="legend"> &#11036; <em> Idle </em> &emsp; &#128999; <em> Busy </em></p>
            </div>

    </div>
    
</body>
</html>
