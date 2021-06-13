anychart.onDocumentReady(function() {

    var myVar = document.getElementById("myVar").value;
    var myVar1 = document.getElementById("myVar1").value;

    // set the data
    var data = [
        {x: "Number of Correct Submissions", value: myVar,
        normal:  {
           fill: "#2bca3f",      
        },
        hovered: {
           fill: "#2bca3f",
           
           outline: {
             enabled: true,
             width: 6,
             fill: "#2bca3f",
             stroke: null
           }
        },
        selected: {
           outline: {
             enabled: true,
             width: 6,
             fill: "#2bca3f",
             stroke: null
           }
        }
       },
       {x: "Number of Wrong Submissions", value: myVar1,
        normal:  {fill: "#f9433f"},
        hovered: {
          fill: "#f9433f",
          outline: {
             enabled: false
          }
        },
        selected: {outline: {enabled: false}}
       }
    ];
  
    // create the chart
    var chart = anychart.pie();
  
    // set the chart title
    chart.title("Assesment Report");
  
    // add the data
    chart.data(data);
  
    // display the chart in the container
    chart.container('container');
    chart.draw();
  
  });