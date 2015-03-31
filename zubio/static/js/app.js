var zubioHome = angular.module('zubioHome', ['angucomplete-alt']);

zubioHome.config(['$locationProvider', function($locationProvider) {
	$locationProvider.html5Mode(true);
}]);

zubioHome.controller('homeCtrl', ['$scope', '$timeout', function ($scope, $timeout) {
	$scope.query = '';
	$scope.search = function(query){
		if(query){
			$scope.query = query;
 		}
 		$timeout(function(){
 			$('#searchForm').submit()
 		}, 1);
 	};

 	$scope.show = function(elem){
 		$(elem).fadeIn("fast");
 	}

 	$scope.hide = function(elem){
 		$(elem).fadeOut("fast");
 	}
}]);
