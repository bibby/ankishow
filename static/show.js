$(function()
{
  loadData(startInterval);
});

var data;
function loadData(callback)
{
  $.get({
    url: "/data",
    success: function(d)
    {
      data = d;
      callback();
    }
  });
};

function nextItem()
{
    var item = data.shift();
    $(".tpl").each(function()
    {
      $(this).text(item.shift());
    });
};


var _intv;
function startInterval()
{
  _intv = setInterval(nextItem, 1000 * 4);
};

function stopInterval()
{
  stopInterval(_intv);
};
