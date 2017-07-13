/**
 * Created by scant on 17-7-9.
 */
function initialize_map() {
    console.log("imap:" + testValue);
    var mapVal = "testValue of Map";
    //$(window.parent.document).find("div.mapVal").text("1223");
    //window.parent.document.getElementById("mapVal").innerHTML = mapVal;
    var map = new BMap.Map("odoo-baidu-map");
    var point = new BMap.Point(116.404, 39.915);
    map.centerAndZoom(point, 15)
}
initialize_map();
