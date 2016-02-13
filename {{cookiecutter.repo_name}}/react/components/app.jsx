/* global gettext, $ */
var React = require('react');

var App = React.createClass({
  propTypes: {
    children: React.PropTypes.any,
    route: React.PropTypes.object
  },

  getInitialState: function () {
    return {urls: {}};
  },

  componentWillMount: function () {
    var self = this;
    var url = {% if cookiecutter.use_translation == 'True' %}'/' + this.props.route.language + {% endif %}'/api/urls/';
    $.get(url, function (response) {
      self.setState({urls: response});
    });
  },

  render: function () {
    return (
      <div className="site-wrapper-inner">
        <div className="cover-container">
          <div className="masthead clearfix">
            <div className="inner">
              <h3 className="masthead-brand">{gettext('Home')}</h3>
              <nav>
                <ul className="nav masthead-nav">
                  <li className="active"><a href="">{gettext('Home')}</a></li>
                  <li>
                    <a href={this.state.urls.admin_index}>{gettext('Admin')}</a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
          <div className="inner cover">
            {React.cloneElement(this.props.children, {urls: this.state.urls})}
          </div>
        </div>
      </div>);
  }
});
module.exports = App;
