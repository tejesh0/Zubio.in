var zubioHome = angular.module('zubioHome', ['angucomplete-alt']);

zubioHome.config(['$locationProvider', function($locationProvider) {
	$locationProvider.html5Mode(true);
}]);

// zubioHome.controller('homeCtrl', ['$scope', function ($scope) {
	
// }]);