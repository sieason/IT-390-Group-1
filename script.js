// Code goes here
angular.module('MasterDetailDemo', ['ui.router'])
.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
  $urlRouterProvider.otherwise('/blog/list');
  var states = [
    {
      abstract: true,
      name: 'wrapper',
      url: '/blog',
      template: "<h1>Master Detail Interface</h1><ui-view></ui-view>",
      controller: 'wrapperController'
    },{
      name: 'wrapper.master',
      url: '/list',
      template: "<ol><li ng-repeat='post in data'><h2><a ui-sref='wrapper.detail({id: {{post.id}}})'>{{post.title}}</a></h2></li></ol>"
    },{
      name: 'wrapper.detail',
      url: '/{:id}',
      template: "<a ui-sref='wrapper.master'><- Back to list</a><br><h2>{{post.title}}</h2><p>{{post.body}}</p>",
      controller: 'detailController'
    }
  ];
  states.forEach((state) => $stateProvider.state(state));

}]).controller('wrapperController', ['$scope', '$timeout', function($scope, $timeout) {
  $scope.data;
  //Mimic asyncronous GET request
  $timeout(() => {
    $scope.data = [
      {
        id: 0,
        title: 'AMD Radeon RX 6400',
        body: 'Released in Jan 2022 for the price of $159. 16 MB of Cache. 4 GB Memory'
      },{
        id: 1,
        title: 'AMD Radeon RX 6600',
        body: 'Released in August 2021 for the price of $329. 32 MB of Cache. 8 GB Memory '
      },{
        id: 2,
        title: 'AMD Radeon RX 6700',
        body: 'Released in June 2022 for the price of $599. 80 MB of Cache. 10 GB of Memory'
      }
    ];
  }, 3000);
  
}]).controller('detailController', ["$scope", "$stateParams", function($scope, $stateParams) {
  var post_id = $stateParams.id;

  if ($scope.data) {
    $scope.post = $scope.data[post_id];
  }
}]);