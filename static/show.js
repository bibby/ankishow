var slide_time = 1000 * 8;
var transition_time = 500;
var colors = [
  '7FFFD4', 'FFE4C4', '2020DF', '8A2BE2',
  'DEB887', '5F9EA0', '7FFF00', 'FF7F50',
  'D2691E', '6495ED', '008B8B', 'A9A9A9',
  'FF8C00', '9932CC', 'E9967A', '8FBC8F',
  '00CED1', 'ADFF2F', 'FF69B4', 'CD5C5C',
  'F0E68C', '7CFC00', 'ADD8E6', 'F08080',
  '90EE90', 'FFB6C1', '87CEFA', '32CD32',
  '66CDAA', 'BA55D3', '9370D8', '3CB371',
  '00FA9A'
];

Array.prototype.shuffle = function() {
  var i = this.length, j, temp;
  if ( i == 0 ) return this;
  while ( --i ) {
     j = Math.floor( Math.random() * ( i + 1 ) );
     temp = this[i];
     this[i] = this[j];
     this[j] = temp;
  }
  return this;
};

$(function()
{
  $("body").keypress(keyPress);
  loadData(function()
  {
    nextItem();
    startInterval();
  });
});

var data;
function loadData(callback)
{
  console.info("loading data");
  $.get({
    url: "/data",
    success: function(d)
    {
      data = d;
      console.info("data loaded");
      if(callback instanceof Function)
        callback();
    }
  });
};

var item_hist = [];
var hist_index = undefined;
function nextItem()
{
    var item = data.shift();
    nextColor();

    item_hist.push([item, color]);
    while(item_hist.length > 20)
      item_hist.shift();
    hist_index = item_hist.length - 1;
    setText(item);

    if (!data.length)
      loadData();
};

function setText(item)
{
  fadeCard(getCard(active_card));
  console.log(item);
  nextCard()
  .fadeIn(transition_time)
  .find(".tpl")
  .each(function(i)
  {
    $(this).text(item[i]);
  });
}

var color;
function nextColor(){
  var c = colors.shuffle()[0];
  if(c != color)
  {
    color = c;
    return setColor(c);
  }

  nextColor();
};

function setColor(to)
{
  $("#display").animate(
    {
      backgroundColor: "#" + to
    },
    transition_time
  );
}

var _intv;
function startInterval()
{
  if(!_intv)
  {
    console.info('starting');
    _intv = setInterval(nextItem, slide_time);
  }
};

function stopInterval()
{
  if(_intv)
  {
    console.info('stopping');
    clearInterval(_intv);
    _intv = undefined;
  }
};

function keyPress(e)
{
  if ( event.which == 13 ) {
     event.preventDefault();
  }
  switch(event.which)
  {
    case 122: // z, pause
      stopInterval();
      break;

    case 120: // x, back
      stopInterval();
      historyBack();
      break;

    case 99: // c, next
      stopInterval();
      historyForward();
      break;

    case 118: // v, resume
      startInterval();
      break;
  }
}

function historyBack()
{
  hist_index = Math.max(0, hist_index - 1);
  console.log("back", hist_index);
  historyItem();
};

function historyForward()
{
  hist_index = Math.min(item_hist.length - 1, hist_index + 1);
  console.log("forward", hist_index);
  historyItem();
};

function historyItem()
{
  var item = item_hist[hist_index];
  if(item)
  {
      setText(item[0]);
      setColor(item[1]);
  }
}

var active_card = 0;
var card_names =  ['a', 'b'];
function getCard(c)
{
  return $("#" + card_names[c]);
};

function nextCard()
{
  active_card = Math.abs(active_card - 1);
  return getCard(active_card);
};

function fadeCard($c)
{
  $c.fadeOut(transition_time, function()
  {
    $(this).find(".tpl").text('');
  });
}
