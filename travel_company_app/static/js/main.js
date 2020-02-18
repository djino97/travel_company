/*This part of code is used to create a slick carousel of items*/
$(".slider").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    dots: true,
});


let myApp = angular.module('MyApp', ['ngMaterial', 'ngMessages', 'ngStorage']);

myApp.controller('AppCtrl', function ($scope) {
    $scope.eventClass = function () {
        $scope.myDate = new Date();

        $scope.minDate = new Date(
            $scope.myDate.getFullYear(),
            $scope.myDate.getMonth() - 2,
            $scope.myDate.getDate());

        $scope.maxDate = new Date(
            $scope.myDate.getFullYear(),
            $scope.myDate.getMonth() + 2,
            $scope.myDate.getDate());

        $scope.onlyWeekendsPredicate = function (date) {
            let day = date.getDay();
            return day === 0 || day === 6;
        }
    };

});

myApp.controller('accountCtrl', function ($scope) {
let originatorEv;

    $scope.openMenu = function($mdMenu, ev) {
        originatorEv = ev;
        $mdMenu.open(ev);
    };
    $scope.display = angular.element(document.querySelector(".md_menu"))
    $scope.display.css("display","block")
});