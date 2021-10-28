var current_stats={}
var player_select=d3.select('#selDataset')
d3.json('/fetch').then(data=>{
    // console.log(data)
    var fullname_list=Object.values(data['FullName'])
    for (var i=0; i<fullname_list.length; i++){
        player_select.append('option').text(fullname_list[i]).property('value', fullname_list[i])
    }
    // var object=data.FullName
    // var name_list=Object.keys(object)
    // var dropdown_list=d3.select('#selDataset')
    // for (var i=0; i=name_list.length; i++){
    //     dropdown_list.append('option').attr('value', name_list[i]).text(name_list[i])
    // }
})

function optionChanged(fullname){
    d3.json(`/player_stats/${fullname}`).then(stats_json=>{
        // iteate through the object to display key <> value
        current_stats=stats_json
        console.log(current_stats)
    })
}

function prediction(){
    console.log(current_stats)
    // current_stats has 40 elements that are not sorted in the order of the X_train features
    // /prediciton endpoint takes ?param=value&param=value&param=value
    var query_string='abc'
    d3.json(`/sample/${query_string}`).then(result=>{
        d3.select('#new_overall_rating').text(result['output'])
    })
}