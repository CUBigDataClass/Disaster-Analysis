var disasterAnalysis = angular.module('disasterAnalysis', []);

disasterAnalysis.controller('displayGraphsController',function ($scope,$http) {
  $scope.sendInfo = function() 
	{
		/*$http.get("getCount")
		.then(function(response) 
    		{
       	 		$scope.content = response.data;
			console.log($scope.content)
    		});
		*/
		//var data = JSON.stringify({ name: $scope.search})
		//console.log(data)	
		//$http.post("getCount/", data)
		//.then(function(data, status) 
		//{
            	//	$scope.content = data;
		//	console.log($scope.content)
       		// });
		
		//#console.log($scope.search)
		/*$http.post('/getCount/', 
		{
       			search: $scope.search
    		})
		.success(function(data, status, headers, config)
		{
			console.log(data);
		})*/
		console.log($scope.content)
	}
});
