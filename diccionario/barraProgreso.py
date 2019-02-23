
class BarraProgreso(object):

    def printProgressBar(self, iteration, total, prefix = '',
                           suffix = 'Completado', decimals = 0,
                           length = 40, fill = '■'):

        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)

        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
        
        # Print New Line on Complete
        if iteration == total:  print()
