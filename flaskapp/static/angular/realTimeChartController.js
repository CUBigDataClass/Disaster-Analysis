var disasterAnalysis = angular.module('disasterAnalysis', []);

disasterAnalysis.controller('realTimeChartController', ['$scope','$http', function ($scope,$http) {

(function ()
{
                $http({ 
                        method: 'GET',
                        url: '/getRealSecondJSONforAll'
                        }).then(function successCallback(response)
                        {
				//console.log("hello");
                                getDonut(response.data)
                        }, function errorCallback(response) {
                     });
})();


setInterval(function ()
	{
		$http({
  			method: 'GET',
  			url: '/getRealSecondJSONforAll'
			}).then(function successCallback(response) 
			{
				getDonut(response.data)
    			}, function errorCallback(response) {
                     });
	},10000);
}]);
