<!DOCTYPE html>
	<html>
		
	<style type="text/css">

    div.Outer {
        width: 640px;
        position: relative;
        clear: both;
        }

        div.InnerLeft {
        width: 300px;
        height:300px;
        margin:10px;
        position: relative;
        background: #CCCCCC;        
        float: left;
        } 

        div.InnerRight {
        width: 300px;
        height:300px;
        margin:10px;
        position: relative;
        background: #AAAAFF;        
        float: right;
        }

    </style>
	
		
	<body>

%for url, value in zipped:	
	<div class = 'Outer'>	
		<div class = 'InnerLeft'>
			<img src = '{{url}}' height = '300px;'>
		</div>
	
		<div class = 'InnerRight' style='background-color: rgb({{value}});'>
		</div>

	</div>
%end

	</body>
	
</html>
