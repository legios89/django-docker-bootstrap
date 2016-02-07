var React = require('react');
var ReactDOM = require('react-dom');
var Router = require('react-router');
var Route = Router.Route;
var browserHistory = Router.browserHistory;


var App = React.createClass({
  render: function () {
    return (<div>Proba</div>);
  }
});

ReactDOM.render((
  <Router history={browserHistory}>
    <Route path="/" component={App}/>
  </Router>
), document.body);
