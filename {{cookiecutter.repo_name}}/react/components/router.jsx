/* global gettext */
var React = require('react');
var ReactDOM = require('react-dom');
var ReactRouter = require('react-router');
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var createHashHistory = require('history/lib/createHashHistory');

// Components
var App = require('./app.jsx');
var Home = require('./home.jsx');


var NotFoundRoute = React.createClass({
  render: function () {
    return (<div>{gettext('NOT FOUND')}</div>);
  }
});

var history = createHashHistory({
  queryKey: false
});

ReactDOM.render((
  <Router history={history}>
    <Route component={App}>
      <Route path="/" component={Home}/>
      <Route path="*" component={NotFoundRoute}/>
    </Route>
  </Router>), document.getElementById('app-place'));
