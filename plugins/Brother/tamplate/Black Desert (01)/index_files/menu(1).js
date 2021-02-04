var jqGaijinMenu = $('.gaijin-menu');

var jqGameList = $('.js-games-list', jqGaijinMenu);

var gameItem = jqGameList.children(),
    countsOfGameLists = jqGameList.length;

var gameItemWidth = gameItem.width(),
    gameItemCount = gameItem.length;

jqGameList.width(Math.floor((gameItemWidth * gameItemCount + gameItemCount - 1) / (countsOfGameLists || 1)));

var dropList,
    allDroplists = $('.top-panel__item > .top-panel__drop-list', jqGaijinMenu),
    allTopPanelLinks = $('.top-panel__link', jqGaijinMenu);

$(document).click(function () {

    menuDropListShowOff();
});

$(window).on('resize', function () {

    gaijinMenuWidth = jqGaijinMenu.width();
    gaijinMenuOffset = jqGaijinMenu.offset();

}).resize();

allTopPanelLinks.off().on('click', linkEvent);

function fixDirection(jqLink) {

    var rightSpace = gaijinMenuWidth - jqLink.parent().offset().left + gaijinMenuOffset.left;
    var linkDropDownContent = jqLink.next();

    if (linkDropDownContent.hasClass('top-panel__drop-list') && rightSpace > 0) {

        if (rightSpace > linkDropDownContent.width()) {

            linkDropDownContent.css('right', 'inherit');

        } else {

            linkDropDownContent.css('right', 0);
        }
    }
}

function menuDropListShowOff() {
    allDroplists.fadeOut();
    allTopPanelLinks.removeClass('active');
}

function showCurrentMenuDropList(object) {

    if (object instanceof jQuery) {

        object.toggleClass('active');
        object.parent().toggleClass('active');
    }

    if(dropList instanceof jQuery) {

        dropList.fadeIn();
    }
}

function linkEvent(e) {

    dropList = $(this).next();

    if (dropList.hasClass('top-panel__drop-list')) {

        fixDirection($(this));

        e.preventDefault();
        e.stopPropagation();

        if ($(this).hasClass('active')) {
            menuDropListShowOff();
        } else {
            menuDropListShowOff();
            showCurrentMenuDropList($(this));
        }
    }
}